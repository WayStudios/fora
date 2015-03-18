$(document).ready(function() {
  $("#form-user-registration > .form-group > #input-email").change(function(){
    var email = $(this).val();
  });
  $("#submit-form-user-registration").click(function() {
    var email = $("#form-user-registration > .form-group > #input-email").val();
    var username = $("#form-user-registration > .form-group > #input-username").val();
    var password = $("#form-user-registration > .form-group > #input-password").val();
    var confirmPassword = $("#form-user-registration > .form-group > #input-confirm-password").val();
    var acceptPolicies = $("#checkbox-accept-policies").is(":checked");

    console.log(email);
    console.log(username);
    console.log(password == confirmPassword);
    console.log(acceptPolicies);

    if (password == confirmPassword && acceptPolicies) {
      $.ajax({
        url: "?action=create_user",
        type: "POST",
        data: JSON.stringify({
          "email": email,
          "username": username,
          "password": password,
          "acceptPolicies": acceptPolicies
        }),
        contentType: 'application/json; charaset=utf-8',
        success: function(data) {
          
        }
      });
    }
  });
});
