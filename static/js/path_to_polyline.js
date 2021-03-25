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

    if (window.DOMParser)
    {
        parser = new DOMParser();
        input_svg = parser.parseFromString(path, "text/xml");
    }
    
    var paths = input_svg.getElementsByTagName("path")
    var pol, cursor

    for (var i = 0; i < paths.length; i++)
    {
        var d = paths[i].getAttribute("d");
        console.log(d);
    }
}