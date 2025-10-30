
"""
AI Entropy Data Collection Module
Collects system and user data for entropy generation
"""

import time
import numpy as np
from collections import deque

class EntropyDataCollector:
    def __init__(self):
        self.mouse_events = deque(maxlen=1000)
        self.system_metrics = deque(maxlen=500)
        self.collection_active = False
        
    def start_collection(self):
        """Start background data collection"""
        self.collection_active = True
        print("🔍 AI Entropy Data Collection Started")
        
    def stop_collection(self):
        """Stop data collection"""
        self.collection_active = False
        print("🛑 AI Entropy Data Collection Stopped")
    
    def add_mouse_event(self, x, y):
        """Add mouse movement data"""
        if self.collection_active:
            event_data = {
                'timestamp': time.time(),
                'x': x, 'y': y,
                'type': 'mouse_move'
            }
            self.mouse_events.append(event_data)
    
    def collect_system_metrics(self):
        """Collect system-level entropy data"""
        if self.collection_active:
            # Simulate system metrics collection
            metric_sample = {
                'timestamp': time.time(),
                'cpu_jitter': np.random.randint(1, 100),  # Will be real measurements
                'memory_variation': np.random.randint(1, 100),
                'time_nanoseconds': time.time_ns() % 1000
            }
            self.system_metrics.append(metric_sample)
    
    def get_entropy_data(self):
        """Get all collected entropy data"""
        return {
            'mouse_events_count': len(self.mouse_events),
            'system_metrics_count': len(self.system_metrics),
            'status': 'active' if self.collection_active else 'inactive'
        }

# Global instance
entropy_collector = EntropyDataCollector()
