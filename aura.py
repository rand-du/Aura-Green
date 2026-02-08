# ---------------------------------------------------------
# Project: Aura-Green
# Purpose: Ethical AI Energy & Carbon Emission Tracking
# Status: Production / Professional Prototype
# ---------------------------------------------------------

class AuraGreenMonitor:
    """
    A professional utility to estimate the carbon footprint of AI operations.
    Promoting sustainable and eco-friendly technology development.
    """
    
    # Global average for Carbon Intensity (kg CO2 per kWh)
    CARBON_INTENSITY_FACTOR = 0.475 

    def __init__(self):
        print("--- Aura-Green: Sustainability System Active ---")

    def calculate_impact(self, watts, hours):
        """
        Logic to convert hardware power usage into CO2 emissions.
        """
        # Basic validation to ensure numbers are positive
        if watts < 0 or hours < 0:
            return None
            
        energy_kwh = (watts * hours) / 1000
        co2_kg = energy_kwh * self.CARBON_INTENSITY_FACTOR
        return energy_kwh, co2_kg

    def start_assessment(self):
        """
        Interactive interface for data input and reporting.
        """
        try:
            print("\nPlease enter the operational data:")
            p_watts = float(input("> Hardware Consumption (Watts): "))
            p_hours = float(input("> Operational Duration (Hours): "))
            
            results = self.calculate_impact(p_watts, p_hours)
            
            if results:
                energy, carbon = results
                print("\n" + "="*30)
                print(f"  ENERGY USED:   {energy:.2f} kWh")
                print(f"  CO2 PRODUCED:  {carbon:.4f} kg")
                print("="*30)
                
                if carbon > 5.0:
                    print("ADVICE: High impact detected. Consider efficiency optimization.")
                else:
                    print("ADVICE: Sustainable operation. Environmentally safe.")
            else:
                print("Error: Input values must be positive.")
                
        except ValueError:
            print("Error: Invalid input. Please enter numerical values.")

# Main Execution
if __name__ == "__main__":
    system = AuraGreenMonitor()
    system.start_assessment()
