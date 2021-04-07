var input = document.getElementById("input_file")
var file

input.addEventListener('input', () => {
    file = input.files[0];
    if (file.type != "image/svg+xml")
    {
        window.alert("Wrong type!")
    }
    else
    {
        let reader = new FileReader();
        reader.readAsText(file);

        reader.onload = function() {
            document.getElementById("input_view").outerHTML = reader.result;
            document.getElementsByTagName("svg")[0].setAttribute("id", "input_view");
            pol_from_path(reader.result)
        };
        
        reader.onerror = function() {
            window.alert("File reading error!");
        };
    }
})

function pol_from_path(path)
{
    if (window.DOMParser)
    {
        parser = new DOMParser();
        input_svg = parser.parseFromString(path, "text/xml");
    }
    
    var paths = input_svg.getElementsByTagName("path");
    var html_paths = document.getElementById("input_view").getElementsByTagName("path");

    for (var i = 0; i < paths.length; i++)
    {
        var d = paths[i].getAttribute("d").substr(2);
        console.log(d);
        
        var pol = "";
        var cx = 0.0, cy = 0.0;

        d = d.replaceAll(',', ' ');

        while (d.length > 0)
        {
            cx += parseFloat(d);
            d = removeFloat(d).substr(1);
            cy += parseFloat(d);
            d = removeFloat(d).substr(1);
            pol += cx + "," + cy + " "; 
        }

        html_paths[0].removeAttribute("d");
        html_paths[0].setAttribute("points", pol);
        html_paths[0].outerHTML = html_paths[0].outerHTML.replaceAll("path", "polyline");
        html_paths = document.getElementById("input_view").getElementsByTagName("path");
    }
}

function removeFloat(s)
{
    while (s.length > 0 && "0123456789+-.,e".indexOf(s[0]) != -1)
    {
        s = s.substr(1);
    }
    return s;
}