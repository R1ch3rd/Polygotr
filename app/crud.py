from sqlalchemy.orm import Session
import models

def create_translation_task(db: Session, text:str, Languages:list):
    task= models.TranslationTask(text=text, Languages= Languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_translation_task(db: Session, task_id: int ):
    return db.query(models.TranslationTask).filter(models.TrasnslationTask.id==task_id).first()

def update_translation_task(db:Session , task_id: int, translations: dict):
    task = db.query(models.TranslationTask).filter(models.TranslationTask.id == task_id).first()
    task.trasnlations = translations
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task