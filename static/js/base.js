/**
 * Created by nonex_000 on 1/13/2015.
 */
function load_data() {
    alert("starting data load")
    $("#data_holder").load("/api/something/test_worked!", function(responseTxt,statusTxt,xhr){
    if(statusTxt=="success")
      alert("External content loaded successfully!");
    if(statusTxt=="error")
      alert("Error: "+xhr.status+": "+xhr.statusText);
  });

}