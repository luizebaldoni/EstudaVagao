from app.models import Post

def searchFunction(request):
    search_context = {}
    posts = Post.objects.all()
    if "search" in request.GET:
        query = request.GET.get("q")
        #filtragem começa aqui
        search_box = request.GET.get("search-box")
        if search_box == "Tudo":
            objects = posts.filter(content__icontains=query)
        else:
            objects = posts.filter(title__icontains=query)
        
        #termina aqui
        search_context = {
            "objects":objects,
            "query":query,
        }
    return search_context