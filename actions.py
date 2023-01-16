from fastapi import HTTPException, status


from models import Menus, SubMenus, Dishes


def get_item(model, db, target_id):
    """Get a menu, submenu or dish item

    target_id depend on model.id
    """
    item = db.query(model).filter(model.id == target_id).first()

    if item:
        if model == Dishes:
            return {"id": str(item.id),
                    "title": item.title,
                    "description": item.description,
                    "price": str(item.price)}
        elif model == SubMenus:
            return {"id": str(item.id),
                    "title": item.title,
                    "description": item.description,
                    "dishes_count": db.query(Dishes).count()}
        elif model == Menus:
            return {"id": str(item.id),
                    "title": item.title,
                    "description": item.description,
                    "submenus_count": db.query(SubMenus).count(),
                    "dishes_count": db.query(Dishes).count()}

    if model == Dishes:
        word = "dish"
    elif model == Menus:
        word = "menu"
    elif model == SubMenus:
        word = "submenu"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{word} not found")


def create_item(model, schema, db, item_id=None):
    """Create a menu, submenu or dish item

    item_id depends on model.id

    """
    if model == Menus:
        new_menu = Menus(
            title=schema.title,
            description=schema.description
        )
    elif model == SubMenus:
        new_menu = SubMenus(
            title=schema.title,
            description=schema.description,
            menu_id=item_id
        )
    elif model == Dishes:
        new_menu = Dishes(
            title=schema.title,
            description=schema.description,
            sub_menu_id=item_id,
            price=round(schema.price, 2)
        )

    db.add(new_menu)
    db.commit()
    return new_menu


def update_item(model, schema, db, item_id):
    if model == Dishes:
        db.query(model).filter(model.id == item_id).update({"title": schema.title,
                                                            "description": schema.description,
                                                            "price": round(schema.price, 2)})
    else:
        db.query(model).filter(model.id == item_id).update({"title": schema.title, "description": schema.description})

    db.commit()
    upd_menu = db.query(model).filter(model.id == item_id).first()
    return upd_menu


def delete_item(model, db, item_id):
    db.query(model).filter(model.id == item_id).delete()
    db.commit()
