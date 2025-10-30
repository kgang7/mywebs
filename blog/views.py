from django.shortcuts import render

# Create your views here.
def blog_view(request):
    posts = Post.object.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    posts = Post.object.all()
    context = {'posts':posts}
    return render(request,'test.html', context)

