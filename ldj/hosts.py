from django_hosts import patterns, host

host_patterns = patterns("",
    host(r"", "ldj.urls", name="ldj"),
    host(r"dictionary", "dict.urls", name="dict"),
    host(r"seo", "seo.urls", name="seo"),
)