import uvicorn
from fastapi import FastAPI, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

import schemas
import actions
from database import sessionLocal
from models import Menus, SubMenus, Dishes

app = FastAPI(
    title="Menu App"
)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup():
    """Cleared DB when server starts"""
    db = sessionLocal()
    db.query(Menus).delete()
    db.query(SubMenus).delete()
    db.query(Dishes).delete()
    db.commit()
    db.close()


@app.get("/api/v1/menus", status_code=200)
def get_all_menu(db: Session = Depends(get_db)):
    output = db.query(Menus).all()

    return output


@app.get("/api/v1/menus/{target_menu_id}")
def get_target_menu(target_menu_id: int, db: Session = Depends(get_db)):
    return actions.get_item(Menus, db, target_menu_id)


@app.post("/api/v1/menus", status_code=status.HTTP_201_CREATED)
def create_menu(menu: schemas.MenuSchema, db: Session = Depends(get_db)):
    nm = actions.create_item(Menus, menu, db)
    return {"id": str(nm.id),
            "title": nm.title,
            "description": nm.description}


@app.patch("/api/v1/menus/{target_menu_id}")
def update_menu(target_menu_id: int, menus: schemas.MenuSchema, db: Session = Depends(get_db)):
    upd_menu = actions.update_item(Menus, menus, db, target_menu_id)
    return {"title": upd_menu.title,
            "description": upd_menu.description}


@app.delete("/api/v1/menus/{target_menu_id}")
def delete_menu(target_menu_id: int, db: Session = Depends(get_db)):
    actions.delete_item(Menus, db, target_menu_id)


@app.post("/api/v1/menus/{target_menu_id}/submenus", status_code=status.HTTP_201_CREATED)
def create_sub_menu(target_menu_id: int, submenu: schemas.SubMenuSchema, db: Session = Depends(get_db)):
    new_submenu = actions.create_item(SubMenus, submenu, db, target_menu_id)
    return {"id": str(new_submenu.id),
            "title": new_submenu.title,
            "description": new_submenu.description}


@app.get("/api/v1/menus/{target_menu_id}/submenus")
def show_all_submenus(target_menu_id: int, db: Session = Depends(get_db)):
    submenus = db.query(SubMenus).filter(SubMenus.menu_id == target_menu_id).all()
    return submenus


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
def show_submenu(target_submenu_id: int, db: Session = Depends(get_db)):
    return actions.get_item(SubMenus, db, target_submenu_id)


@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
def update_submenu(target_submenu_id: int, submenu: schemas.SubMenuSchema, db: Session = Depends(get_db)):
    upd_submenu = actions.update_item(SubMenus, submenu, db, target_submenu_id)
    return {"title": upd_submenu.title,
            "description": upd_submenu.description}


@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
def delete_submenu(target_submenu_id: int, db: Session = Depends(get_db)):
    actions.delete_item(SubMenus, db, target_submenu_id)


@app.post("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes", status_code=status.HTTP_201_CREATED)
def create_dish(target_submenu_id: int, dish: schemas.DishesSchema, db: Session = Depends(get_db)):
    new_dish = actions.create_item(Dishes, dish, db, target_submenu_id)
    return {"id": str(new_dish.id),
            "title": new_dish.title,
            "description": new_dish.description,
            "price": str(new_dish.price)}


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes")
def show_all_dishes(target_submenu_id: int, db: Session = Depends(get_db)):
    dishes = db.query(Dishes).filter(Dishes.sub_menu_id == target_submenu_id).all()
    return dishes


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
def show_dish(target_dish_id: int, db: Session = Depends(get_db)):
    return actions.get_item(Dishes, db, target_dish_id)


@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
def update_submenu(target_dish_id: int, submenu: schemas.DishesSchema, db: Session = Depends(get_db)):
    upd_dish = actions.update_item(Dishes, submenu, db, target_dish_id)
    return {"title": upd_dish.title,
            "description": upd_dish.description,
            "price": str(upd_dish.price)}


@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
def delete_submenu(target_dish_id: int, db: Session = Depends(get_db)):
    actions.delete_item(Dishes, db, target_dish_id)


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
