document.getElementById('upload-form').addEventListener('submit', function(e){

    e.preventDefault();

    let formData = new FormData(this);
    console.log(formData);


    //to view the image
    let fileInput = document.getElementById('input-file');
    let file = fileInput.files[0];
    let reader = new FileReader();

    reader.onload = function(event) {
        let imgElement = document.getElementById('selected-image');
        imgElement.src = event.target.result;
        imgElement.style.display = 'block'; // Show the image
    }

    if (file) {
        reader.readAsDataURL(file);
    }
    //to code end here
    

    fetch('/upload',{
        method:'POST',
        body: FormData
    })

    .then(response => response.json() )
    .then (data => {
        document.getElementById('result-container').innerText = 'Result: ' + data.result;
    })
    .catch(error => {
        console.log('Error',error);
    })
}) 