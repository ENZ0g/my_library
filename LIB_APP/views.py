from django.http import HttpResponse
from django.template import loader
from .models import Author, Book, Redaction, BookHolder
from .forms import AuthorForm, RedactionForm, BookHolderForm, BookForm
from django.db.models import Sum
from django.urls import reverse_lazy
from datetime import datetime as dt
from django.http.response import HttpResponseRedirect


def books_list(request):
    template = loader.get_template('books.html')
    books = {'books': Book.objects.all()}
    books.update(Book.objects.all().aggregate(Sum('copy_count')))
    return HttpResponse(template.render(books, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return HttpResponseRedirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return HttpResponseRedirect(reverse_lazy('main'))
            book.copy_count += 1
            book.save()
        return HttpResponseRedirect(reverse_lazy('main'))
    else:
        return HttpResponseRedirect(reverse_lazy('main'))


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return HttpResponseRedirect(reverse_lazy('main'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return HttpResponseRedirect(reverse_lazy('main'))
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return HttpResponseRedirect(reverse_lazy('main'))
    else:
        return HttpResponseRedirect(reverse_lazy('main'))


def redactions_list(request):
    template = loader.get_template('redactions.html')

    if request.method == 'POST':
        name = request.POST['name']
        Redaction.objects.create(name=name)
        return HttpResponseRedirect(reverse_lazy('redactions'))
    else:
        redactions = Redaction.objects.all()
        data = {'redactions': [],
                'form': RedactionForm()}
        for redaction in redactions:
            data['redactions'].append({'name': redaction,
                                       'books': Book.objects.filter(redaction=redaction)})
        return HttpResponse(template.render(data, request))


def is_latin(string):
    """
    Возвращает True, если строка string состоит из прописных или строчных
    латинских букв (без пробелов), иначе - False
    """
    length = len(string)
    for i in string:
        if ord(i) in range(65, 91) or ord(i) in range(97, 123):
            length -= 1
    if length == 0:
        return True
    else:
        return False


def author_list(request):
    template = loader.get_template('authors.html')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            birth_year = request.POST['birth_year']
            country = request.POST['country']
            print(type(country), country.isdigit())
            if country.isdigit() or not is_latin(country):
                form.add_error(field='country',
                               error='Введите 2 латинские буквы')
                data = {'authors': Author.objects.all(),
                        'form': form}
                return HttpResponse(template.render(data, request))
            Author.objects.create(full_name=full_name,
                                  birth_year=birth_year,
                                  country=country)
            return HttpResponseRedirect(reverse_lazy('authors'))
        else:
            data = {'authors': Author.objects.all(),
                    'form': form}
    else:
        data = {'authors': Author.objects.all(),
                'form': AuthorForm()}
    return HttpResponse(template.render(data, request))


def readers_list(request):
    template = loader.get_template('readers.html')

    if request.method == 'POST':
        form = BookHolderForm(request.POST)
        if form.is_valid():
            new_name = request.POST['name']
            try:
                new_birth_date = dt.strptime(request.POST['birth_date'], '%d.%m.%Y')
            except ValueError:
                new_birth_date = dt.strptime(request.POST['birth_date'], '%d,%m,%Y')
            BookHolder.objects.create(name=new_name,
                                      birth_date=new_birth_date)
            return HttpResponseRedirect(reverse_lazy('readers'))
        else:
            data = {'readers': BookHolder.objects.all(),
                    'form': form}
            return HttpResponse(template.render(data, request))
    else:
        readers = BookHolder.objects.all()
        data = {'readers': [],
                'form': BookHolderForm()}
        for reader in readers:
            data['readers'].append({'name': reader.name,
                                    'birth_date': reader.birth_date,
                                    'books': Book.objects.filter(reader=reader)})
        return HttpResponse(template.render(data, request))


def new_book(request):
    template = loader.get_template('new_book.html')

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('main'))
        else:
            data = {'form': form,
                    'form_not_valid': True}
            return HttpResponse(template.render(data, request))
    else:
        data = {'form': BookForm()}
    return HttpResponse(template.render(data, request))
