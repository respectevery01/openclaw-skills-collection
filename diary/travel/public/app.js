document.addEventListener('DOMContentLoaded', function() {
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const travelPlan = document.getElementById('travelPlan');
    const metadata = document.getElementById('metadata');
    const tripInfo = document.getElementById('tripInfo');
    const routeSection = document.getElementById('routeSection');
    const weatherSection = document.getElementById('weatherSection');
    const attractionsSection = document.getElementById('attractionsSection');
    const itinerarySection = document.getElementById('itinerarySection');
    const summarySection = document.getElementById('summarySection');

    const urlParams = new URLSearchParams(window.location.search);
    const planFile = urlParams.get('plan');

    if (planFile) {
        loadTravelPlan(planFile);
    } else {
        loadLatestTravelPlan();
    }

    async function loadTravelPlan(filename) {
        showLoading(true);
        hideError();
        hideTravelPlan();

        try {
            const response = await fetch(`/api/travel-plan/${filename}`);
            const data = await response.json();

            if (response.ok) {
                displayTravelPlan(data);
            } else {
                showError(data.error || 'Failed to load travel plan');
            }
        } catch (err) {
            showError('Network error, please try again later');
            console.error('Error:', err);
        } finally {
            showLoading(false);
        }
    }

    async function loadLatestTravelPlan() {
        showLoading(true);
        hideError();
        hideTravelPlan();

        try {
            const response = await fetch('/api/travel-plans');
            const plans = await response.json();

            if (response.ok && plans.length > 0) {
                const latestPlan = plans[0];
                await loadTravelPlan(latestPlan.filename);
            } else {
                showError('No travel plans found. Please create a travel plan first.');
            }
        } catch (err) {
            showError('Network error, please try again later');
            console.error('Error:', err);
        } finally {
            showLoading(false);
        }
    }

    function displayTravelPlan(data) {
        displayMetadata(data.metadata);
        displayTripInfo(data.trip_info);
        displayRoute(data.route);
        displayWeather(data.weather);
        displayAttractions(data.attractions);
        displayItinerary(data.daily_itinerary);
        displaySummary(data.summary);
        showTravelPlan();
    }

    function displayMetadata(metadata) {
        if (!metadata) return;

        metadata.innerHTML = `
            <div class="metadata-card">
                <h2>📋 ${metadata.title || 'Travel Plan'}</h2>
                <p class="description">${metadata.description || ''}</p>
                <p class="created-date">Created: ${metadata.created_date || 'Unknown'}</p>
            </div>
        `;
    }

    function displayTripInfo(tripInfo) {
        if (!tripInfo) return;

        const waypointsHtml = tripInfo.waypoints && tripInfo.waypoints.length > 0 
            ? tripInfo.waypoints.map(wp => `<span class="waypoint">${wp}</span>`).join(' → ')
            : '';

        tripInfo.innerHTML = `
            <div class="trip-info-card">
                <h2>🗺️ Trip Information</h2>
                <div class="trip-details">
                    <div class="trip-detail">
                        <strong>Origin:</strong>
                        <span>${tripInfo.origin || 'Unknown'}</span>
                    </div>
                    <div class="trip-detail">
                        <strong>Destination:</strong>
                        <span>${tripInfo.destination || 'Unknown'}</span>
                    </div>
                    ${waypointsHtml ? `
                    <div class="trip-detail">
                        <strong>Waypoints:</strong>
                        <div class="waypoints">${waypointsHtml}</div>
                    </div>
                    ` : ''}
                    <div class="trip-detail">
                        <strong>Duration:</strong>
                        <span>${tripInfo.total_days || 0} days</span>
                    </div>
                    <div class="trip-detail">
                        <strong>Travel Mode:</strong>
                        <span>${tripInfo.travel_mode || 'Unknown'}</span>
                    </div>
                </div>
            </div>
        `;
    }

    function displayRoute(route) {
        if (!route) return;

        let segmentsHtml = '';
        if (route.segments && route.segments.length > 0) {
            segmentsHtml = route.segments.map((segment, index) => `
                <div class="route-segment">
                    <div class="segment-header">
                        <strong>Segment ${index + 1}:</strong> ${segment.from} → ${segment.to}
                    </div>
                    <div class="segment-details">
                        <div class="segment-detail">
                            <strong>Distance:</strong> ${segment.distance || 0} ${segment.distance_unit || 'km'}
                        </div>
                        <div class="segment-detail">
                            <strong>Time:</strong> ${segment.time_formatted || 'Unknown'}
                        </div>
                    </div>
                </div>
            `).join('');
        }

        routeSection.innerHTML = `
            <div class="route-card">
                <h2>🚗 Route Information</h2>
                <div class="route-summary">
                    <div class="route-summary-item">
                        <strong>Total Distance:</strong>
                        <span>${route.total_distance || 0} ${route.total_distance_unit || 'km'}</span>
                    </div>
                    <div class="route-summary-item">
                        <strong>Total Time:</strong>
                        <span>${route.total_time_formatted || 'Unknown'}</span>
                    </div>
                </div>
                ${segmentsHtml ? `
                <div class="route-segments">
                    <h3>Route Segments</h3>
                    ${segmentsHtml}
                </div>
                ` : ''}
            </div>
        `;
    }

    function displayWeather(weather) {
        if (!weather) return;

        let html = '<div class="weather-card"><h2>🌤️ Weather Forecast</h2>';

        Object.entries(weather).forEach(([city, cityData]) => {
            html += `
                <div class="city-weather">
                    <h3>📍 ${cityData.city_name || city}</h3>
                    <div class="weather-summary">
                        <div class="weather-stat">
                            <strong>Average Temperature:</strong>
                            <span>${cityData.average_temp || 'N/A'}°C</span>
                        </div>
                        <div class="weather-stat">
                            <strong>Conditions:</strong>
                            <span>${(cityData.weather_conditions || []).join(', ')}</span>
                        </div>
                    </div>
                    <div class="weather-forecast">
            `;

            if (cityData.forecast && cityData.forecast.length > 0) {
                cityData.forecast.forEach(day => {
                    const date = new Date(day.date);
                    const formattedDate = `${date.getMonth() + 1}/${date.getDate()}`;
                    
                    html += `
                        <div class="weather-day">
                            <div class="day-date">${formattedDate}</div>
                            <div class="day-temp">${day.temp_min}°C ~ ${day.temp_max}°C</div>
                            <div class="day-condition">${day.condition}</div>
                            <div class="day-wind">${day.wind_direction} ${day.wind_scale}</div>
                        </div>
                    `;
                });
            }

            html += `
                    </div>
                </div>
            `;
        });

        html += '</div>';
        weatherSection.innerHTML = html;
    }

    function displayAttractions(attractions) {
        if (!attractions) return;

        let html = '<div class="attractions-card"><h2>🎯 Recommended Attractions</h2>';

        Object.entries(attractions).forEach(([city, cityAttractions]) => {
            html += `
                <div class="city-attractions">
                    <h3>📍 ${city}</h3>
                    <div class="attractions-list">
            `;

            if (cityAttractions && cityAttractions.length > 0) {
                cityAttractions.forEach(attraction => {
                    html += `
                        <div class="attraction-item">
                            <h4>${attraction.name}</h4>
                            <p class="attraction-address">📍 ${attraction.address || 'Unknown'}</p>
                            ${attraction.description ? `<p class="attraction-description">${attraction.description}</p>` : ''}
                            ${attraction.recommended_visit_time ? `
                            <p class="attraction-time">⏱️ Recommended: ${attraction.recommended_visit_time}</p>
                            ` : ''}
                        </div>
                    `;
                });
            }

            html += `
                    </div>
                </div>
            `;
        });

        html += '</div>';
        attractionsSection.innerHTML = html;
    }

    function displayItinerary(itinerary) {
        if (!itinerary) return;

        let html = '<div class="itinerary-card"><h2>📅 Daily Itinerary</h2>';

        itinerary.forEach(day => {
            html += `
                <div class="day-itinerary">
                    <div class="day-header">
                        <h3>Day ${day.day}</h3>
                        <span class="day-date">${day.date}</span>
                    </div>
                    <div class="day-location">
                        <strong>📍 Location:</strong> ${day.location}
                    </div>
                    <div class="day-weather">
                        <strong>🌤️ Weather:</strong> ${day.weather_summary || 'Unknown'}
                    </div>
                    <div class="day-activities">
            `;

            if (day.activities && day.activities.length > 0) {
                day.activities.forEach(activity => {
                    html += `
                        <div class="activity-item">
                            <div class="activity-time">${activity.time}</div>
                            <div class="activity-content">
                                <strong>${activity.activity}</strong>
                                <span class="activity-type">${activity.type}</span>
                            </div>
                            ${activity.weather ? `
                            <div class="activity-weather">🌤️ ${activity.weather}</div>
                            ` : ''}
                        </div>
                    `;
                });
            }

            html += `
                    </div>
                </div>
            `;
        });

        html += '</div>';
        itinerarySection.innerHTML = html;
    }

    function displaySummary(summary) {
        if (!summary) return;

        let recommendationsHtml = '';
        if (summary.recommendations && summary.recommendations.length > 0) {
            recommendationsHtml = summary.recommendations.map(rec => `
                <li>${rec}</li>
            `).join('');
        }

        summarySection.innerHTML = `
            <div class="summary-card">
                <h2>📊 Trip Summary</h2>
                <div class="summary-stats">
                    <div class="summary-stat">
                        <strong>Total Locations:</strong>
                        <span>${summary.total_locations || 0}</span>
                    </div>
                    <div class="summary-stat">
                        <strong>Total Attractions:</strong>
                        <span>${summary.total_attractions || 0}</span>
                    </div>
                    <div class="summary-stat">
                        <strong>Average Temperature:</strong>
                        <span>${summary.average_temperature || 'N/A'}°C</span>
                    </div>
                    <div class="summary-stat">
                        <strong>Weather Conditions:</strong>
                        <span>${(summary.weather_conditions || []).join(', ')}</span>
                    </div>
                    <div class="summary-stat">
                        <strong>Total Distance:</strong>
                        <span>${summary.total_distance || 0} km</span>
                    </div>
                    <div class="summary-stat">
                        <strong>Total Time:</strong>
                        <span>${summary.total_time || 'Unknown'}</span>
                    </div>
                </div>
                ${recommendationsHtml ? `
                <div class="recommendations">
                    <h3>💡 Recommendations</h3>
                    <ul>${recommendationsHtml}</ul>
                </div>
                ` : ''}
            </div>
        `;
    }

    function showLoading(show) {
        if (show) {
            loading.classList.remove('hidden');
        } else {
            loading.classList.add('hidden');
        }
    }

    function showTravelPlan() {
        travelPlan.classList.remove('hidden');
    }

    function hideTravelPlan() {
        travelPlan.classList.add('hidden');
    }

    function showError(message) {
        error.textContent = message;
        error.classList.remove('hidden');
    }

    function hideError() {
        error.classList.add('hidden');
    }
});