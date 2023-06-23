# HttpRequest in Python (Flask), ReactJS, NodeJS, php (CI)
as always just jump in to the codes...
## Python (Flask)
There's some solutions in [this py file](https://github.com/samanshahin/HttpRequest-in-Python-Flask-ReactJS-NodeJS-php-CI-/blob/main/http.py), and you can use it...
## ReactJS
There's some solutions:
### A- getting data:
#### -1- using fetch in js:
You can access the code [here](https://github.com/samanshahin/HttpRequest-in-Python-Flask-ReactJS-NodeJS-php-CI-/blob/main/http.js).
#### -2- using XMLHttpRequest in js:
Use this code sample in your html file:
```
<script>
function loadXMLDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML =
      this.responseText;
    }
  };
  xhttp.open("GET", "xmlhttp_info.txt", true);
  xhttp.send();
}
</script>
```
#### -3- WebSockets: 
refer to [this link](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
### B- sending data (being used as an RESTapi serverless):
#### -1- react router:
Better to check [this repo](https://github.com/remix-run/react-router/tree/dev/examples/data-router)
#### -2- inner-app solution: 
If you want to request data inner app, you should make request to "redux" or "json". I would suggest you [this repo](https://github.com/samanshahin/Redux-in-ReactJS) for ReactJS or [this repo](https://github.com/samanshahin/Redux-in-ReactNative) for React Native.
