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
    var d = "";

    var i = 0;
    while (html_paths.length > 0)
    {
        var pol = "";
        var pols = [];
        var cx = 0.0, cy = 0.0;

        d = paths[i].getAttribute("d").replaceAll(',', ' ').trim().substr(1).trim();

        while (d.length > 0)
        {
            if (d[0] == "m")
            {
                pols.push(pol);
                //console.log(pol);
                //console.log("12321");
                pol = "";
                d = d.substr(1).trim();
            }

            if (d[0] == "z")
            {
                pol += " " + pol.split(" ")[0];
                console.log(pol);
                d = d.substr(1).trim();

                cx = parseFloat(pol.split(",")[0]);
                cx = parseFloat(pol.split(",")[1]);
                continue;
            }

            /*
            console.log("###")
            console.log(d);
            console.log(pol);
            console.log("###" + cx + " " + cy + "###");
            

            if (isNaN(cx))
            {
                //console.log(d);
                //console.log(pol);
                var answer = prompt('question', 'defaultAnswer');
            }
            */

            cx += parseFloat(d);
            d = removeFloat(d).substr(1).trim();
            cy += parseFloat(d);
            d = removeFloat(d).substr(1).trim();
            pol += cx + "," + cy + " ";
        }

        pols.push(pol);
        //console.log(pol);

        //console.log(pols);

        for (var j = 0; j < pols.length; j++)
        {
            var polyline = document.createElement("polyline");

            {
                function cloneAttributes(element, sourceNode) {
                    let attr;
                    let attributes = Array.prototype.slice.call(sourceNode.attributes);
                    while(attr = attributes.pop()) {
                        element.setAttribute(attr.nodeName, attr.nodeValue);
                    }
                }

                cloneAttributes(polyline, html_paths[0]);
            }

            console.log(polyline);

            polyline.removeAttribute("d");
            polyline.removeAttribute("id");
            polyline.setAttribute("points", pols[j]);

            html_paths[0].parentElement.appendChild(polyline);
        }
        

        html_paths[0].parentNode.removeChild(html_paths[0]);
        html_paths = document.getElementById("input_view").getElementsByTagName("path");
        i++;
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