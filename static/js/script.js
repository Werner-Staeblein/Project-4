document.addEventListener('DOMContentLoaded', function () {
    // Collect all the delete buttons and store in constant

    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {

            // Step 1: Prevent default action of the link = NO immediate naviagte to delete URL
            event.preventDefault();

            const commentId = button.getAttribute('data-comment-id');
            const deleteUrl = "{% url 'delete_comment' post.slug 0 %}".replace("0", commentId);

            // Step 2: Set the href attribute of the delete button in the modal
            const deleteConfirmButton = document.getElementById('deleteConfirm');
            deleteConfirmButton.setAttribute('href', deleteUrl);

            // Step 3: Make the modal visible
            const deleteModal = new bootstrap.Modal(document.getElementById('ModalForDelete'));
            deleteModal.show();
        });
    });
});