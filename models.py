from sqlalchemy import MetaData, Column, Integer, String, Text, ForeignKey, Numeric

from database import Base

metadata = MetaData()


class Menus(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text)

    def __repr__(self):
        return f"<Menus title={self.title} description={self.description}>"


class SubMenus(Base):
    __tablename__ = "sub menus"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text)
    menu_id = Column(Integer, ForeignKey(Menus.id, ondelete="CASCADE"))

    def __repr__(self):
        return f"<Menus title={self.title} description={self.description}>"


class Dishes(Base):
    __tablename__ = "dishes",
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(Text)
    sub_menu_id = Column(Integer, ForeignKey(SubMenus.id, ondelete="CASCADE"))
    price = Column(Numeric, nullable=False)

    def __repr__(self):
        return f"<Menus title={self.title} description={self.description}>"
