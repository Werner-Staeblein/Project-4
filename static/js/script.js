document.addEventListener('DOMContentLoaded', function () {

    
    function setDeleteUrl(commentUrl) {
        const deleteConfirmButton = document.getElementById('deleteConfirm');
        deleteConfirmButton.setAttribute('href', commentUrl);
    }

    // 
    document.querySelectorAll('.delete-button').forEach(button => {
        button.addEventListener('click', function() {
    
            // 
            const commentUrl = this.getAttribute('data-comment-url');
    
            // 
            setDeleteUrl(commentUrl);
    
            // 
            const modal = new bootstrap.Modal(document.getElementById('ModalForDelete'));
            modal.show();
        });
    });

});
