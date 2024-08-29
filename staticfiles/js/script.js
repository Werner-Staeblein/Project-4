document.querySelectorAll('.delete-button').forEach(button => {
    button.addEventListener('click', function() {
        const commentUrl = this.getAttribute('data-comment-url');
        const deleteConfirmButton = document.getElementById('deleteConfirm');
        deleteConfirmButton.setAttribute('href', commentUrl);
        const modal = new bootstrap.Modal(document.getElementById('ModalForDelete'));
        modal.show();
    });
});
