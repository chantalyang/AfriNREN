from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from django.db.models import Sum
from AfriNREN_Vis.models import Flow
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
    ASNs = list(set(['AS%d' % random.randint(1000, 50000) for x in range(50)]))
    Countries = ["South Africa", "Zimbabwe", "Kenya",
                 "United Kingdom", "Netherlands", "Nigeria",
                 "Botswana", "Somalia"]

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
              } for x in range(0, 50)]

    routes = [{"src": random.choice(ASNs),
               "dst": random.choice(ASNs),
               "hops": [{"ASN": random.choice(ASNs)} for x in range(1, 4)]}
              for y in range(10, 30)]

    # for route in routes:
    #     links.append({"source": route.src,
    #                   "target": route.hops[0],
    #                   })

    nodesjson = json.dumps(nodes)
    linksjson = json.dumps(links)

    data = {'nodes': nodes,
            'links': links,
            'routes': routes}

    return data


def graphjson(request):
    return JsonResponse(graphRDG())


def graph(request):
    return render(request, "testtemplates/p_graph.html")


def graph2(request):
    return render(request, "p_graph2.html")


def allconvograph(request):
    return render(request, "p_allconvograph.html")


def getTopSrcs():
    '''
    Return list of source ASNs with the top most traffic
    transferred.
    '''
    top_srcs = []
    try:
        top_srcs_obs = Flow.objects.values('source_asn')\
            .annotate(sum_bytes=Sum('bytes_transferred'))\
            .order_by('-sum_bytes')[0:20]
    except IndexError:
        top_srcs_obs = None

    for ob in top_srcs_obs:
        top_srcs.append(ob['source_asn'])
    return top_srcs


def getTopDstsPerTopSrc():
    '''
    Return dictionary linking source ASNs to a list of their
    top conversation partners (destination ASNs).
    '''
    tops = {}
    top_dst_asns = []
    top_src_asns = getTopSrcs()
    top_flow_obs = Flow.objects\
        .filter(source_asn__in=top_src_asns)\
        .values('source_asn', 'destination_asn')\
        .annotate(sum_bytes=Sum('bytes_transferred'))\
        .order_by('-bytes_transferred')
    for ob in top_flow_obs:
        try:
            # limit list of destination ASNs to 5
            dst_ASNs = tops[ob['source_asn']]
            if len(dst_ASNs) < 5:
                tops[ob['source_asn']].append(ob['destination_asn'])
        except KeyError:
            tops[ob['source_asn']] = [ob['destination_asn']]
    for src in tops.keys():
        top_dst_asns.extend(tops[src])
    top_dst_asns = list(set(top_dst_asns))
    return tops


def getListOfImportantASNs():
    nb_asns = []


def getData(request):
    return HttpResponse(getTopDstsPerTopSrc())
