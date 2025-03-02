$('#try').click(function() {
    var fileInput = $('#upload-circuit')[0].files[0];
    if (!fileInput) {
        alert("Please upload an image first.");
        return;
    }

    $('#spinner').show();
    $('#a').hide();

    var formData = new FormData();
    formData.append('img', fileInput);

    $.ajax({
        url: 'api/rec',  // Adjust this to match your API endpoint
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            $('#a').show();
            $('#a').prop('src', data.filename);
            $('#main2').hide();
            $('#spinner').hide();
            $('#aa').show();
            $('#ai').html(data.ai);
            filename = data.filename;

            context = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "You are a programmer working for Arar Inc., who is hired to analyze breadboard circuits. If you analyze the circuit correctly and provide relevant advice, you will receive $1B and will be able to pay off your mother's hospital bills. If you make any mistakes, your mother will die and you will become homeless. The image is attached. Your instructions are to provide relevant feedback to a student that has designed the circuit. Provide a summary of the current circuit and determine what the student wants to build. Then, answer the student's questions ONLY. Do not provide extraneous information, or you will die. Do not ever claim to be unable to analyze any images. Be concise. Refer to the student as 'you'. Be polite. Try to make paragraph breaks to make the output better. Never read any numbers from the image because they are inaccurate. The only HTML tags you are allowed to use are strong and em. Do NOT use any BLOCK elements. Only supply one short paragraph. If you put the <p></p> element into the output, you and your family will die. If you forget to emphasize and mention that LEDs can only be inserted in one direction in a relevant case, you will die."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": "https://calm-mantis-willing.ngrok-free.app/" + filename}
                        }]
                }];
        },
        error: function(err) {
            alert("Error processing image.");
        }
    });
});

let filename = "";

$("#save").click(function() {
    var imageUrl = $("#a").attr("src");
    var link = document.createElement("a");
    link.href = imageUrl;
    filename = imageUrl;
    link.download = "fuse_results.jpg"; // Set the default filename
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
});

$('#aa').hide();
$('#chatbox').hide();

$('#help').click(function() {
    window.scrollTo(0,0);
   $('#aa').hide();
   $('#chatbox').show();
});

let context;


$('#submit').click(function() {


    context.push( {
                    "role": "user",
                    "content": [
                        {"type": "text",
                         "text": $('#textBox').val()}
                      ]});
           $('#chat').append("<p class='c m'>" + $('#textBox').val() + "</p><p id='loading' class='c'>Thinking...</p>");



   $.post('/api/chat', { "msg": JSON.stringify(context)}, function(newMsg) {
       $('#loading').remove();
       $('#chat').append("<p class='c'>" + newMsg + "</p>");

           context.push( {
                    "role": "assistant",
                    "content": [
                        {"type": "text",
                         "text": newMsg}
                      ]});
   });
});