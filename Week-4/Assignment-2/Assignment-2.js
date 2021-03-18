function ajax(src, callback){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
                var data = JSON.parse(this.responseText);
                if (callback) callback(data);
            }
        };
    xhttp.open('GET', src, true);
    xhttp.send(); 
    }

function render(data){
    const main = document.querySelector("#main");
    
    // create title for table
    var trNode = document.createElement("TR");
    if (data) {
        for (var key in data[0]) {
            var thNode = document.createElement("TH");
            thNode.innerHTML = key;
            trNode.appendChild(thNode); 
        }
    }
    main.appendChild(trNode);

    // create entries
    for (var i = 0; i < data.length; i += 1) {
        var trNode = document.createElement("TR"); 
        if (data) {   
            for (var key in data[i]) {
                var tdNode = document.createElement("TD");
                tdNode.innerHTML = data[i][key];
                trNode.appendChild(tdNode);                          
            }
        main.appendChild(trNode);
        }
    }
}

ajax("http://13.113.12.180:4000/api/1.0/remote-w4-data", function(response){ 
    render(response);
}); 