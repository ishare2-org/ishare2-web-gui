$('#confirmDownloadModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget) // Button that triggered the modal
    let id = button.data('index') // Extract info from data-* attributes
    let name = button.data('name') ? button.data('name') : button.data('foldername') // Extract info from data-* attributes
    let type = button.data('type') // Extract info from data-* attributes
    let size = button.data('size') // Extract info from data-* attributes
    let unit = button.data('size-unit') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    let modal = $(this)
    // modal.find('.modal-title').text('New message to ' + recipient)
    // modal.find('.modal-body input').val(recipient)
    modal.find('#image-name').val(name)
    modal.find('#image-type').val(type)
    modal.find('#image-size').val(size + ' ' + unit)
    modal.find('#ishare-command').val('ishare2 pull ' + type + ' ' + id)
    modal.find('.btn-success').click(function () {
        downloadImage(id, name, type)
    })
})
$('#confirmDeleteModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget) // Button that triggered the modal
    let id = button.data('index') // Extract info from data-* attributes
    let name = button.data('name') ? button.data('name') : button.data('foldername') // Extract info from data-* attributes
    let type = button.data('type') // Extract info from data-* attributes
    let size = button.data('size') // Extract info from data-* attributes
    let unit = button.data('size-unit') // Extract info from data-* attributes
    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    let modal = $(this)
    // modal.find('.modal-title').text('New message to ' + recipient)
    // modal.find('.modal-body input').val(recipient)
    modal.find('#image-name').val(name)
    modal.find('#image-type').val(type)
    modal.find('#image-size').val(size + ' ' + unit)
    modal.find('#ishare-command').val('ishare2 pull ' + type + ' ' + id)
    modal.find('.btn-danger').click(function () {
        deleteImage(id, name, type)
    })
})

function downloadImage(id, name, type) {
    $.ajax({
        url: '/download/' + type + '/' + id,
        type: 'GET',

        success: function (result) {
            let msgclass;
            result.status > 0 ? msgclass = "error" : msgclass = "success";
            $.notify(result.message, {
                position: "bottom right",
                style: "bootstrap",
                className: msgclass,
                autoHide: true
            });
        }
    });
}
function deleteImage(id, name, type) {
    $.ajax({
        url: '/delete/' + type + '/' + id,
        type: 'GET',
        success: function (result) {
            let msgclass;
            result.status > 0 ? msgclass = "error" : msgclass = "success";
            $.notify(result.message, {
                position: "bottom right",
                style: "bootstrap",
                className: msgclass,
                autoHide: true
            });
        }
    });
}