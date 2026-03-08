const express = require('express');
const path = require('path');
const cors = require('cors');
const fs = require('fs');
require('dotenv').config({ path: path.join(__dirname, '../../.env') });

const app = express();
const PORT = process.env.TRAVEL_PORT || 3001;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

function mergeTravelPlan(modulesDir) {
    try {
        const metadata = JSON.parse(fs.readFileSync(path.join(modulesDir, 'metadata.json'), 'utf8'));
        const tripInfo = JSON.parse(fs.readFileSync(path.join(modulesDir, 'trip-info.json'), 'utf8'));
        const route = JSON.parse(fs.readFileSync(path.join(modulesDir, 'route.json'), 'utf8'));
        const weather = JSON.parse(fs.readFileSync(path.join(modulesDir, 'weather.json'), 'utf8'));
        const attractions = JSON.parse(fs.readFileSync(path.join(modulesDir, 'attractions.json'), 'utf8'));
        const itinerary = JSON.parse(fs.readFileSync(path.join(modulesDir, 'itinerary.json'), 'utf8'));
        const summary = JSON.parse(fs.readFileSync(path.join(modulesDir, 'summary.json'), 'utf8'));

        return {
            metadata,
            trip_info: tripInfo,
            route,
            weather,
            attractions,
            daily_itinerary: itinerary,
            summary
        };
    } catch (error) {
        console.error('Error merging travel plan modules:', error);
        throw new Error('Failed to merge travel plan modules');
    }
}

app.get('/api/travel-plan/:filename', (req, res) => {
    try {
        const filename = req.params.filename;
        const filePath = path.join(__dirname, '../assets', `${filename}.json`);
        
        if (fs.existsSync(filePath)) {
            const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
            res.json(data);
        } else {
            res.status(404).json({ error: 'Travel plan not found' });
        }
    } catch (error) {
        console.error('Error reading travel plan:', error);
        res.status(500).json({ error: 'Failed to read travel plan' });
    }
});

app.get('/api/travel-plan/modules/:planName', (req, res) => {
    try {
        const planName = req.params.planName;
        const modulesDir = path.join(__dirname, '../assets/modules');
        
        if (!fs.existsSync(modulesDir)) {
            return res.status(404).json({ error: 'Modules directory not found' });
        }

        const travelPlan = mergeTravelPlan(modulesDir);
        res.json(travelPlan);
    } catch (error) {
        console.error('Error reading modular travel plan:', error);
        res.status(500).json({ error: 'Failed to read modular travel plan' });
    }
});

app.get('/api/travel-plans', (req, res) => {
    try {
        const assetsDir = path.join(__dirname, '../assets');
        const files = fs.readdirSync(assetsDir)
            .filter(file => file.endsWith('.json') && file !== 'example.json' && !file.startsWith('modules'))
            .sort((a, b) => {
                const statA = fs.statSync(path.join(assetsDir, a));
                const statB = fs.statSync(path.join(assetsDir, b));
                return statB.mtime - statA.mtime;
            });
        
        const plans = files.map(file => {
            const filePath = path.join(assetsDir, file);
            const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
            return {
                filename: file.replace('.json', ''),
                title: data.metadata?.title || file,
                created_date: data.metadata?.created_date || '',
                origin: data.trip_info?.origin || '',
                destination: data.trip_info?.destination || '',
                days: data.trip_info?.total_days || 0
            };
        });
        
        res.json(plans);
    } catch (error) {
        console.error('Error listing travel plans:', error);
        res.status(500).json({ error: 'Failed to list travel plans' });
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen(PORT, () => {
    console.log(`Travel planning server running on port ${PORT}`);
    console.log(`Open http://localhost:${PORT} in your browser`);
});
