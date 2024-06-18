$(function(){
    $("#submit").click(chatWithLLM);
    $("message").keypress(function(e){
        if(e.which == 13){
            chatWithLLM
        }
    })
})