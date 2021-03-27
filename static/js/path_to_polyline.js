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
            pol_from_path(reader.result)
        };
        
        reader.onerror = function() {
            window.alert("File reading error!");
        };
    }
})

function pol_from_path(path)
{
    var samples = 100;

    if (window.DOMParser)
    {
        parser = new DOMParser();
        input_svg = parser.parseFromString(path, "text/xml");
    }
    
    var paths = input_svg.getElementsByTagName("path")
    var pol = "";
    var pols = [];


    console.log(paths.length)
    for (var i = 0; i < 1; i++)
    {
        var d = paths[i].getAttribute("d");
        var command;
        var cx = 0, cy = 0;

        var i = 0;

        while (i < 1)
        {
            command = d[0];
            d = d.substr(1);

            switch (command)
            {
                case 'm':
                    if (pol != "")
                    {
                        pols.push(pol.trim());
                        pol = "";
                    }

                    cx += parseFloat(d);
                    cy += parseFloat(d);

                    break;
                case 'M':
                    if (pol != "")
                    {
                        pols.push(pol.trim());
                        pol = "";
                    }

                    cx = parseFloat(d);
                    cy = parseFloat(d);

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
                case 'V ':
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
                    pol.trim();
                    pol += pol.split(' ')[0];
                    break;
                case 'z':
                    pol.trim();
                    pol += pol.split(' ')[0];
                    break;
                case 'c':
                    var dtemp = 'M' + cx + ' ' + cy + ' c ';

                    dtemp += (cx += parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy += parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cx += parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy += parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cx += parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy += parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();

                    pathtemp = document.createElementNS("http://www.w3.org/2000/svg", "path");
                    pathtemp.setAttribute("d", dtemp);

                    pol += TempPathToPol(pathtemp, samples)

                    break;
                case 'C':
                    var dtemp = 'M' + cx + ' ' + cy + ' c ';

                    dtemp += (cx = parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy = parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cx = parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy = parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cx = parseFloat(d)) + ' ';
                    d = removeFloat(d);
                    d = d.trim();

                    dtemp += (cy = parseFloat(d));
                    d = removeFloat(d);
                    d = d.trim();

                    pathtemp = document.createElementNS("http://www.w3.org/2000/svg", "path");
                    pathtemp.setAttribute("d", dtemp);

                    pol += TempPathToPol(pathtemp, samples)

                    break;
                default:
                    console.log(command);
                    break;
            }
            i++;
        }
    }

    function removeFloat (s)
    {
        while (s.length > 0 && "0123456789+-.,e".indexOf(s[0]) != -1)
        {
            s = s.substr(1);
        }
        return s;
    }

    function TempPathToPol(path, samples)
    {
        var samp_len = path.getTotalLength / samples, ans, point;

        for (var i = 1; i < samples; i++)
        {
            point = path.getPointAtLength(samp_len * i);
            ans += ' ' + point.x + ',' + point.y;
        }
        return ans;
    }
}