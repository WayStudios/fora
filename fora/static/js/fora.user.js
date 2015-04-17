$(document).ready(function() {
  $("#button-login-submit").click(function(){
    var form = $("#form-login");
    var identity = form.find("#input-identity").val();
    var password = form.find("#input-password").val();
    $.ajax({
      url: "/user/?action=login_user",
      type: "POST",
      data: JSON.stringify({
        "identity": identity,
        "password": password
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          $("#alert-login-invalid-credential").hide();
          $("#alert-login-success").show();
          document.location.reload();
        } else {
          $("#alert-login-success").hide();
          $("#alert-login-invalid-credential").show();
        }
      }
    });
  });

  $("#nav-logout").click(function(){
    $.ajax({
      url: "/user/?action=logout_user",
      type: "POST",
      data: JSON.stringify({
      }),
      contentType: 'application/json; charaset=utf-8',
      success: function(data) {
        if (data.status) {
          document.location.reload();
        }
      }
    });
  });
});
