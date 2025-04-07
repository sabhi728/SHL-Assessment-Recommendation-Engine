document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('recommendationForm');
    const resultsList = document.getElementById('recommendationsList');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Get form values
        const jobRole = document.getElementById('jobRole').value;
        const assessmentNeeds = Array.from(document.getElementById('assessmentNeeds').selectedOptions).map(option => option.value);
        const experienceLevel = document.getElementById('experienceLevel').value;

        // Show loading state
        resultsList.innerHTML = '<div class="loading"><div class="spinner-border loading-spinner" role="status"><span class="visually-hidden">Loading...</span></div></div>';
        resultsDiv.style.display = 'block';

        try {
            // Make API request
            const response = await fetch('/recommend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    job_role: jobRole,
                    assessment_needs: assessmentNeeds,
                    experience_level: experienceLevel
                })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Clear loading state and display results
            resultsList.innerHTML = '';
            
            // Display recommendations
            data.recommended_products.forEach((product, index) => {
                const confidenceScore = data.confidence_scores[index];
                const listItem = document.createElement('div');
                listItem.className = 'list-group-item';
                
                listItem.innerHTML = `
                    <div class="d-flex justify-content-between align-items-start">
                        <div>
                            <h5 class="mb-1">${product.name}</h5>
                            <p class="mb-1">${product.description}</p>
                            <div class="assessment-type">Type: ${product.assessment_type}</div>
                            <div class="assessment-duration">Duration: ${product.duration}</div>
                            <div class="match-details">
                                <strong>Match Details:</strong><br>
                                Semantic Similarity: ${(product.match_details.semantic_similarity * 100).toFixed(1)}%<br>
                                Role Match: ${(product.match_details.role_match * 100).toFixed(1)}%<br>
                                Category Match: ${(product.match_details.category_match * 100).toFixed(1)}%
                            </div>
                        </div>
                        <span class="badge bg-primary rounded-pill confidence-score">
                            ${(confidenceScore * 100).toFixed(1)}% Match
                        </span>
                    </div>
                `;
                
                resultsList.appendChild(listItem);
            });

        } catch (error) {
            resultsList.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    Error getting recommendations. Please try again.
                </div>
            `;
        }
    });
}); 