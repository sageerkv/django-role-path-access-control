function updateStatus(selectElement, ticket_id) {
    const newStatus = selectElement.value;
    const url = `/admin/update_ticket_status/${ticket_id}/`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ status: newStatus }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update ticket status');
        }
        location.reload();
        return response.json();
    })
    .then(data => {
        // Optionally handle success response
        console.log('Ticket status updated successfully:', data);
    })
    .catch(error => {
        console.error('Error updating ticket status:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

