from add_task_strategy import AddTaskStrategy
from models import *
from models.board_meta import BackgroundMeta
from context_factory import ContextFactory
from db_manager import DBManager

___test = 1


def test_decorator():
    print("Testing decorator ...")

    b = Board()
    b.add_task("Wash the car.")
    print(b.to_dict())

    b = BackgroundMeta(
        b,
        "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg")
    print(b.to_dict())

    print("=" * 50)


def test_factory():
    print("Testing factory ...")

    cf = ContextFactory()
    ctx = cf.create_context("userboard")

    print(type(ctx))
    print(dir(ctx))

    print("=" * 50)


def test_singleton_and_proxy_and_builder():
    print("Testing singleton, proxy and builder ...")

    dbm = DBManager.get_instance()
    dbm.create_schema()

    mb = ModelBuilder()
    user = mb.create_model('User', 'UserModel', username="ghadd")
    print(user)

    print("=" * 50)


def test_strategy(username='anon'):
    print("Testing strategy with `username = {}`...".format(username))

    dbm = DBManager.get_instance()
    dbm.create_schema()

    mb = ModelBuilder()
    user = mb.create_model('User', 'UserModel', username=username)
    board = mb.create_model('Board', 'BoardModel', tasks=['initial_task'])

    cf = ContextFactory()
    ctx = cf.create_context("userboard")
    ctx.user_id = user.id
    ctx.object_id = board.id
    ctx.payload = {
        "task": "this is a new task"
    }
    ctx.strategy = AddTaskStrategy()

    ctx.exec()

    print("=" * 50)


def test_memento():
    print("Testing memento ...")

    dbm = DBManager.get_instance()
    dbm.create_schema()

    mb = ModelBuilder()
    user = mb.create_model('User', 'UserModel', username="cool_username")
    board = mb.create_model('Board', 'BoardModel', tasks=['initial_task'])
    caretaker = Caretaker(board)

    caretaker.backup()

    cf = ContextFactory()
    ctx = cf.create_context("userboard")
    ctx.user_id = user.id
    ctx.object_id = board.id
    ctx.payload = {
        "task": "this is a new task"
    }
    ctx.strategy = AddTaskStrategy()

    ctx.exec()
    board = BoardModel.get(board.id)

    caretaker.backup()

    print()
    caretaker.show_history()

    print(board.tasks)
    caretaker.undo()
    board = BoardModel.get(board.id)

    print(board.tasks)

    print("=" * 50)


def test_iterator():
    print("Testing iterator ...")

    dbm = DBManager.get_instance()
    dbm.create_schema()

    mb = ModelBuilder()
    board = mb.create_model('Board', 'BoardModel', tasks=['initial_task1', 'initial_task2', 'initial_task3'])

    print("Iterating board")
    for task in board:
        print(task)

    print("=" * 50)


if __name__ == "__main__":
    test_singleton_and_proxy_and_builder()
    test_factory()
    test_decorator()
    test_strategy('anon')
    test_strategy('cool_username')
    test_memento()
    test_iterator()
