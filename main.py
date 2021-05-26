from add_task_strategy import AddTaskStrategy
from models import *
from models.board_meta import BackgroundMeta
from context_factory import ContextFactory
from db_manager import DBManager


def test_decorator():
    b = Board()
    b.add_task("Wash the car.")
    print(b.to_dict())

    b = BackgroundMeta(
        b,
        "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg")
    print(b.to_dict())


def test_factory():
    cf = ContextFactory()
    ctx = cf.create_context("userboard")

    print(dir(ctx))


def test_singleton_and_proxy_and_builder():
    dbm = DBManager.get_instance()
    dbm.create_schema()

    mb = ModelBuilder()
    user = mb.create_model('User', 'UserModel', username="ghadd")
    print(user)


def test_strategy(username='anon'):
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


def test_memento():
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


if __name__ == "__main__":
    # test_decorator()
    # test_singleton_and_proxy_and_builder()
    # test_factory()

    # test_strategy('anon')
    # test_strategy('cool_username')

    # test_memento()

    pass
