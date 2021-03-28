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
    var samp_len = 10;

    if (window.DOMParser)
    {
        parser = new DOMParser();
        input_svg = parser.parseFromString(path, "text/xml");
    }
    
    var paths = input_svg.getElementsByTagName("path");
    var pol = "";
    var pols = [];
    var html_paths = document.getElementById("input_view").getElementsByTagName("path");

    for (var i = 0; i < paths.length; i++)
    {
        var d = paths[i].getAttribute("d");
        var command;
        var cx = 0, cy = 0;
        var curve = ""

        console.log(d);

        while (d.length > 0)
        {
            command = d[0];
            d = d.substr(1);


            if ("mMlMvVhHzZ".indexOf(command) != -1)
            {
                pol += StringToPol(curve);
                curve = "";
                continue;
            }
            switch (command)
            {
                case 'm':
                    if (pol != "")
                    {
                        pols.push(pol.trim());
                        pol = "";
                    }

                    cx += parseFloat(d);
                    d = removeFloat(d);
                    d = d.trim();

                    cy += parseFloat(d);
                    d = removeFloat(d);
                    d = d.trim();

                    break;
                case 'M':
                    if (pol != "")
                    {
                        pols.push(pol.trim());
                        pol = "";
                    }

                    cx = parseFloat(d);
                    d = removeFloat(d);
                    d = d.trim();

                    cy = parseFloat(d);
                    d = removeFloat(d);
                    d = d.trim();

                    break;
                case 'l':
                    pol += " " + (cx += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();

                    pol += "," + (cy += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
    
                    break;
                case 'L':
                    pol += " " + (cx = parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
    
                    pol += "," + (cy = parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
    
                    break;
                case 'v':
                    pol += " " + cx;
                    
                    pol += "," + (cy += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
        
                    break;
                case 'V':
                    pol += " " + cx;
                    
                    pol += "," + (cy += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
        
                    break;
                case 'h':
                    pol += " " + (cx += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
    
                    pol += "," + cy;

                    break;
                case 'H':
                    pol += " " + (cx = parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();
    
                    pol += "," + cy;
        
                    break;
                case 'Z':
                case 'z':
                    pol.trim();
                    pol += pol.split(' ')[0];
                    break;
                default:
                    curve += command;
                    break;
            }
        }

        pol += StringToPol('M' + cx + ' ' + cy + ' c ' + curve);
        curve = "";

        pol = pol.replace(/(undefined)/gi, '');
        console.log(pol);
        //paths[i].removeAttribute("d");
        //paths[i].setAttribute("points", pol);
        //paths[i].renameNode("path", paths[i].getNamespaceURI, "polyline");

        //document.getElementById("input_view") = s
        html_paths[i].removeAttribute(d);
        html_paths[i].setAttribute("points", pol);
        html_paths[i].outerHTML = html_paths[i].outerHTML.replaceAll("path", "polyline");
        //document.renameNode("path", null, "polyline"); 
    }

    function removeFloat (s)
    {
        while (s.length > 0 && "0123456789+-.,e".indexOf(s[0]) != -1)
        {
            s = s.substr(1);
        }
        return s;
    }

    function TempPathToPol(path)
    {
        //var samp_len = path.getTotalLength() / samples, 
        var ans, point, len = path.getTotalLength();
        console.log(len);
        for (var i = 1; i * samp_len < len; i++)
        {
            point = path.getPointAtLength(samp_len * i);
            ans += ' ' + point.x + ',' + point.y;
        }
        return ans;
    }

    function StringToPol (s)
    {
        s.trim();
        if (s.length == 0)
        {
            return "";
        }

        s = 'M' + cx + ' ' + cy + ' ' + s;

        pathtemp = document.createElementNS("http://www.w3.org/2000/svg", "path");
        pathtemp.setAttribute("d", s);
        return TempPathToPol(pathtemp);
    }
}