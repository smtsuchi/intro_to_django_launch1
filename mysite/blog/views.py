from django.shortcuts import render

# Create your views here.
def index(request):
    my_posts = [
        {
            'author': 'Shoha Tsuchida',
            'title': "This is my first post!",
            'content': "content1",
            'date_posted': "August 9, 2021"
        },
        {
            'author': 'Ivan Wang',
            'title': "This is Ivan's first post!",
            'content': "content from Ivan",
            'date_posted': "August 9, 2021"
        }
    ]
    context = {'posts': my_posts,}
    # <!-- Syntax for adding python vars: {{ var_goes here }} -->
    # <!-- Syntax for adding python vars: {% expression_goes_here %}
    return render(request, 'blog/index.html', context)

def aboutPage(request):
    return render(request, 'blog/about.html')

