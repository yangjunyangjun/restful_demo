from demo.settings import conf


class DB:
    DESK = conf.get("desk", "default")
