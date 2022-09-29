
function myhref(web) {
    url = window.location.href.split('/');
    url[url.lenght - 1] = web
    href = url.join('/')
    window.location.href = url
}

