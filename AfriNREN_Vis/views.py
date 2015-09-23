from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import json
import random


# Create your views here.
def index(request):
    return render(request, "p_index.html")


def stackedrow(request):
    return render(request, "p_d3_stackedrow.html")


def test(request):
    return render(request, "testtemplates/p_testpage.html")


def geo(request):
    return render(request, "index.html")


def graphRDG():
    '''
    Prepare random data to be used within a network graph.
    nodes have ASN, country, name, continent and bytes
    links have src, dst, bytes, latency
    '''
    ASNs = list(set(['AS%d' % random.randint(1000,50000) for x in range(50)]))
    Countries = ["South Africa", "Zimbabwe", "Kenya", "United Kingdom", "Netherlands", "Nigeria", "Botswana", "Somalia"]

    nodes = [{"ASN": ASN,
              "Country": random.choice(Countries),
              "Org": "UCT",
              "Continent": random.choice(['Africa', 'Europe']),
              "Bytes": random.randint(100000000, 100000000000)
              } for ASN in ASNs]

    links = [{"source": random.randint(0, len(nodes)-1),
              "target": random.randint(0, len(nodes)-1),
              "Bytes": random.randint(10000000, 1000000000),
              "Latency": random.randint(5, 500),
              "weight": random.randint(1, 3),
              } for x in range(0,50)]

    nodesjson = json.dumps(nodes)
    linksjson = json.dumps(links)

    data = {'nodes': nodes,
            'links': links}

    return data


def graphjson(request):
    return JsonResponse(graphRDG())


def graph(request):
    return render(request, "testtemplates/p_graph.html")

# def allprobes(request):

#     json_data = open('static/data/all_probes.json')
#     data1 = json.load(json_data)
#     data2 = json.dumps(json_data)

#     json_data.close()
#     return HttpResponse(data1, mimetype='application/json')


# def fibrejson(request):

#     json_data = open('static/data/fibre.json')
#     data1 = json.load(json_data)
#     data2 = json.dumps(json_data)

#     json_data.close()
#     return HttpResponse(data1, mimetype='application/json')
