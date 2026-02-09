const analyzeBtn = document.getElementById('analyzeBtn');
const codeInput = document.getElementById('codeInput');
const analysisType = document.getElementById('analysisType');
const loadingIndicator = document.getElementById('loadingIndicator');
const emptyState = document.getElementById('emptyState');
const resultsContent = document.getElementById('resultsContent');
const issuesContainer = document.getElementById('issuesContainer');
const optimizedCode = document.getElementById('optimizedCode');
const explanationText = document.getElementById('explanationText');

const API_URL = 'http://127.0.0.1:8000';

analyzeBtn.addEventListener('click', async () => {
    const code = codeInput.value;
    const type = analysisType.value;

    if (!code.trim()) {
        alert("Please enter some code to analyze.");
        return;
    }

    // UI Updates: Validation & Loading
    setLoading(true);

    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ code, analysis_type: type })
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API Error: ${response.status} - ${errorText}`);
        }

        const data = await response.json();
        displayResults(data);

    } catch (error) {
        console.error("Analysis failed:", error);
        alert(`Failed to analyze code. \nError: ${error.message}\nMake sure the backend is running at ${API_URL}`);
    } finally {
        setLoading(false);
    }
});

function setLoading(isLoading) {
    if (isLoading) {
        loadingIndicator.classList.remove('hidden');
        resultsContent.classList.add('hidden');
        emptyState.classList.add('hidden');
        analyzeBtn.disabled = true;
        analyzeBtn.classList.add('opacity-75', 'cursor-not-allowed');
        analyzeBtn.innerHTML = '<span class="animate-spin inline-block w-4 h-4 border-2 border-white border-t-transparent rounded-full mr-2"></span>Analyzing...';
    } else {
        loadingIndicator.classList.add('hidden');
        analyzeBtn.disabled = false;
        analyzeBtn.classList.remove('opacity-75', 'cursor-not-allowed');
        analyzeBtn.innerHTML = 'Analyze Code';
    }
}

function displayResults(data) {
    emptyState.classList.add('hidden');
    resultsContent.classList.remove('hidden');

    // 1. Issues
    issuesContainer.innerHTML = '';
    if (data.issues && data.issues.length > 0) {
        data.issues.forEach(issue => {
            const card = document.createElement('div');
            // Determine style based on issue type
            let typeClass = '';
            let borderColor = 'border-red-500';
            let bgColor = 'bg-red-500/10';

            if (issue.type.toLowerCase().includes('warning')) {
                typeClass = 'warning';
                borderColor = 'border-yellow-500';
                bgColor = 'bg-yellow-500/10';
            } else if (issue.type.toLowerCase().includes('style') || issue.type.toLowerCase().includes('info')) {
                typeClass = 'style';
                borderColor = 'border-blue-500';
                bgColor = 'bg-blue-500/10';
            }

            card.className = `p-4 rounded-xl border-l-4 ${borderColor} ${bgColor} mb-3 transition hover:translate-x-1`;
            card.innerHTML = `
                <div class="flex justify-between items-start mb-1">
                    <span class="font-bold text-gray-200 text-xs uppercase tracking-wider bg-black/20 px-2 py-0.5 rounded">${issue.type}</span>
                    <span class="text-xs text-gray-400 font-mono">Line ${issue.line}</span>
                </div>
                <p class="text-sm text-gray-300 mt-1">${issue.message}</p>
            `;
            issuesContainer.appendChild(card);
        });
    } else {
        issuesContainer.innerHTML = `
            <div class="p-4 rounded-xl border border-green-500/30 bg-green-500/10 text-center">
                <p class="text-green-400 font-medium">✨ No issues found! Clean code.</p>
            </div>
        `;
    }

    // 2. Optimized Code
    if (data.optimized_code) {
        optimizedCode.textContent = data.optimized_code;
    } else {
        optimizedCode.textContent = "// No changes suggested.";
    }

    // 3. Explanation
    explanationText.textContent = data.explanation || "No explanation provided.";
}
