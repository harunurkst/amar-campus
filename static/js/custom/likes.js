
function likesCalculator(post_id) {
   var base_url = 'http://localhost:8000/';
  $.ajax({
           type: "GET",
           url: "/api/v1/likes/"+post_id,
           //data: {'id': post_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  console.log(response)
                  var total_likes=response.like_count;
                  document.getElementById('id_'+post_id).innerHTML=total_likes;
                  if(response.is_liked==true) {
                      $('#icon_' + post_id).css('color', 'blue');
                  }
                  else if(response.is_liked==false){
                      $('#icon_' + post_id).css('color', 'black');
                  }
            },
            error: function(rs, e) {
                   alert(rs.responseText);
            }
      });

//})

}

function likeIconChange(post_id){
  console.log("in like icon change");
  $.ajax({
           type: "GET",
           url: "/api/v1/likes/"+post_id,
           //data: {'id': post_id, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
           dataType: "json",
           success: function(response) {
                  if(response.is_liked==true) {
                      $('#icon_' + post_id).css('color', 'blue');
                  }
                  else if(response.is_liked==false){
                      $('#icon_' + post_id).css('color', 'black');
                  }
            },
            error: function(rs, e) {
                   alert(rs.responseText);
            }
      });
}
