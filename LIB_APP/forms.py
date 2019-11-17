from django import forms
from .models import Author, Redaction, BookHolder, Book


class BookForm(forms.ModelForm):

    ISBN = forms.CharField(max_length=13,
                           label='Номер ISBN')
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                            label='Название книги')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'rows': 5}),
                                  label='Описание')
    year_release = forms.IntegerField(label='Год издания',
                                      min_value=0)
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    empty_label='Выберите автора',
                                    label='Автор',
                                    help_text='При отсутствии автора в списке, '
                                              'его можно добавить <a href="../authors">здесь</a>')
    copy_count = forms.IntegerField(label='Количество копий',
                                    min_value=0)
    price = forms.DecimalField(min_value=0,
                               max_digits=6,
                               decimal_places=2,
                               label='Цена')
    redaction = forms.ModelChoiceField(queryset=Redaction.objects.all(),
                                       empty_label='Выберите издательство',
                                       label='Издательство',
                                       help_text='При отсутствии издательства в списке, '
                                                 'его можно добавить '
                                                 '<a href="../redactions">здесь</a>',
                                       )
    reader = forms.ModelChoiceField(queryset=BookHolder.objects.all(),
                                    empty_label='Выберите читателя',
                                    label='Читатель',
                                    help_text='При отсутствии читателя в списке, '
                                              'его можно добавить '
                                              '<a href="../readers">здесь</a>',
                                    required=False
                                    )

    ISBN.widget.attrs.update({'class': 'form-control'})
    year_release.widget.attrs.update({'class': 'form-control'})
    author.widget.attrs.update({'class': 'form-control'})
    copy_count.widget.attrs.update({'class': 'form-control'})
    price.widget.attrs.update({'class': 'form-control'})
    redaction.widget.attrs.update({'class': 'form-control'})
    reader.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                label='Фамилия Имя Отчество автора')
    birth_year = forms.IntegerField(label='Год рождения')
    country = forms.CharField(label='Страна',
                              help_text='Только две латинские буквы. Например: RU')

    birth_year.widget.attrs.update({'class': 'form-control'})
    country.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Author
        fields = '__all__'


class RedactionForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Название издательства')

    class Meta:
        model = Redaction
        fields = '__all__'


class BookHolderForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           label='Фамили Имя Отчество читателя')
    birth_date = forms.DateField(label='Дата рождения',
                                 help_text='ДД.ММ.ГГГГ',
                                 error_messages={'invalid': 'Введите корректную дату и попробуйте снова!'})

    birth_date.widget.attrs.update({'class': 'form-control-sm'})
    birth_date.input_formats = ['%d.%m.%Y', '%d,%m,%Y']

    class Meta:
        model = BookHolder
        fields = '__all__'
