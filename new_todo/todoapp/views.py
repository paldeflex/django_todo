from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Представления для управления задачами в Django-приложении.

def task_list(request):
    # Получаем список всех задач из базы данных.
    tasks = Task.objects.all()
    # Создаем новую форму для ввода задачи.
    form = TaskForm()
    # Проверяем, если метод запроса POST, то обрабатываем форму.
    if request.method == 'POST':
        # Создаем форму с данными из запроса.
        form = TaskForm(request.POST)
        # Проверяем валидность данных формы.
        if form.is_valid():
            # Сохраняем новую задачу в базу данных.
            form.save()
            # Перенаправляем пользователя на список задач.
            return redirect("task-list")
    # Контекст для передачи данных в шаблон.
    context = {"tasks": tasks, "form": form}
    # Отправляем данные на обработку в шаблон и возвращаем результат.
    return render(request, "task_list.html", context)

def task_update(request, pk):
    # Получаем задачу по уникальному ключу или возвращаем ошибку 404.
    task = Task.objects.get(id=pk)
    # Создаем форму для редактирования задачи.
    form = TaskForm(instance=task)
    if request.method == 'POST':
        # Обновляем данные формы с запросом и экземпляром.
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Сохраняем изменения в задаче.
            form.save()
            # Перенаправляем на список задач.
            return redirect("task-list")
    # Контекст для передачи данных в шаблон.
    context = {"form": form}
    # Отправляем данные на обработку в шаблон и возвращаем результат.
    return render(request, "task_list.html", context)

def task_delete(request, pk):
    # Получаем задачу по уникальному ключу.
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        # Удаляем задачу.
        task.delete()
        # Перенаправляем на список задач.
        return redirect("task-list")
    # Контекст для передачи данных в шаблон.
    context = {"task": task}
    # Отправляем данные на обработку в шаблон и возвращаем результат.
    return render(request, "task_delete.html", context)
