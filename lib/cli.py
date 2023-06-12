import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Task, Manager


engine = create_engine('sqlite:///task_manager.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@click.command()
def list_tasks():
    tasks = session.query(Task).all()
    if tasks:
        click.echo("All Tasks:")
        for task in tasks:
            click.echo(task.title)
    else:
        click.echo("No tasks found") 

@click.command()
def list_managers():
    projects = session.query(Manager).all()
    if projects:
        click.echo("All Managers:")
        for manager in manager:
            click.echo(manager.name)
    else:
        click.echo("No managers found")

@click.command()
@click.option("--title", prompt="Enter the task title", help="Task title")
@click.option("--description", prompt="Enter the task description", help="Task description")
@click.option("--status", prompt="Enter the task status", help="Task status")
@click.option("--due-date", prompt="Enter the task due date (YYYY-MM-DD)", help="Task due date")
def add_task(title, description, status, due_date):
    new_task = Task(title=title, description=description, status=status, due_date=due_date)
    session.add(new_task)
    session.commit()
    click.echo("Task added successfully")

@click.command()
@click.option("--task-id", prompt="Enter the task ID", help="Task ID")
def delete_task(task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        click.echo("Task deleted successfully")
    else:
        click.echo("Task not found")

@click.command()
def recent_tasks():
    tasks = session.query(Task).order_by(Task.id.desc()).limit(5).all()
    if tasks:
        click.echo("Recently added tasks:")
        for task in tasks:
            click.echo(task.title)
    else:
        click.echo("No tasks found")

cli.add_command(list_tasks)
cli.add_command(list_managers)
cli.add_command(add_task)
cli.add_command(delete_task)
cli.add_command(recent_tasks)

if __name__ == '__main__':
    cli()