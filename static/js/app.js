const ctx = document.getElementById('wateringChart').getContext('2d');

fetch('/api/watering-intervals')
    .then(response => response.json())
    .then(data => {
        const labels = data.map(item => item.name);
        const intervals = data.map(item => item.interval);

        const wateringChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Watering Intervals (days)',
                    data: intervals,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching watering intervals:', error));