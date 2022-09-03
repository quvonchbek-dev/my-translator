const api_url = "http://127.0.0.1:8000/api/";

function translate_text() {
    var dist = document.getElementById('dist').value
    var src = document.getElementById('src').value
    var text = document.getElementById('src_text').value
    var raw = JSON.stringify({ "dist": dist, "src": src, "text": text });
    var requestOptions = {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: raw,

    };
    fetch(api_url, requestOptions)
        .then(function (response) {
            return response.json()
        })
        .then(function (data) {
             console.log(data)
            translated = document.getElementById("translated_text")
            translated.innerHTML = data.text
        }).catch(error => console.error('Error:', error));
}

function set_dist() {
    dist = document.getElementById('dist')
    dist.value = this.value
    dist.innerHTML = this.text;

}

function set_src() {
    src = document.getElementById('dist')

    dist.value = this.value
    dist.innerHTML = this.text;

}