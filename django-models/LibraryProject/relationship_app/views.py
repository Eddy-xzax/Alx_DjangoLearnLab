from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'list_books': books}
      return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""  
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book.all()
        return context

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # After registration, go to login
    return render(request, 'relationship_app/register.html', {'form': form})
@permission_required('relationship_app.add_book')
def add_book(request):
    # form handling logic here
    return render(request, 'add_book.html')

@permission_required('relationship_app.change_book')
def edit_book(request, book_id):
    # edit logic here
    return render(request, 'edit_book.html')

@permission_required('relationship_app.delete_book')
def delete_book(request, book_id):
    # delete logic here
    return render(request, 'delete_book.html')
