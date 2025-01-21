from django.shortcuts import render
from publications.models import Publication


# Create your views here.
def publication_index(request):
    publications = Publication.objects.all()
    journals = []
    conferences = []
    for publication in publications:
        if publication.is_journal:
            journals.append(publication)
        else:
            conferences.append(publication)
    context = {
        "journals": journals,
        "conferences": conferences
    }
    return render(request, "publications/publication_index.html", context)


def publication_detail(request, pk):
    publication = Publication.objects.get(pk=pk)
    context = {
        "publication": publication
    }

    return render(request, "publications/publication_detail.html", context)
