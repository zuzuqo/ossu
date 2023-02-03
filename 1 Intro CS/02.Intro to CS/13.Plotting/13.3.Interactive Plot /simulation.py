import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Slider

matplotlib.use('TkAgg')


def simulation(fixed, variable):
    infected = [fixed['initial_infections']]
    new_infections = [fixed['initial_infections']]
    total_infections = fixed['initial_infections']

    for t in range(fixed['duration']):
        cur_infections = infected[-1]
        # remove people who are no longer contagious
        if len(new_infections) > fixed['days_spreading']:
            cur_infections -= new_infections[-fixed['days_spreading'] - 1]
        # if social distancing, change number of daily contacts
        if variable['red_start'] <= t < variable['red_end']:
            daily_contacts = variable['red_daily_contacts']
        else:
            daily_contacts = fixed['init_contacts']
        # compute number of new cases
        total_contacts = cur_infections * daily_contacts
        susceptible = fixed['pop'] - total_infections
        risky_contacts = total_contacts * (susceptible / fixed['pop'])
        newly_infected = round(risky_contacts * fixed['contagiousness'])
        # update variables
        new_infections.append(newly_infected)
        total_infections += newly_infected
        infected.append(cur_infections + newly_infected)
    return infected, total_infections


def plot_infections(infections, total_infections, fixed):
    infection_plot = plt.plot(infections, 'r', label='Infected')[0]
    plt.xticks(fontsize='large')
    plt.yticks(fontsize='large')
    plt.xlabel('Days Since First Infection', fontsize='xx-large')
    plt.ylabel('Number Currently Infected', fontsize='xx-large')
    plt.title('Number of Infections Assuming No Vaccine\n' +
              f"Pop = {fixed['pop']:,},"
              f"Contacts/Day = {fixed['init_contacts']},"
              f"Infectivity = {(100 * fixed['contagiousness']):.1f}%,"
              f"Days Contagious = {fixed['days_spreading']}",
              fontsize='xx-large')
    plt.legend(fontsize='xx-large')
    txt_box = plt.text(plt.xlim()[1] / 2, plt.ylim()[1] / 1.25,
                       f"Total Infections = {total_infections:,.0f}",
                       fontdict={'size': 'xx-large', 'weight': 'bold', 'color': 'red'})

    return infection_plot, txt_box

if __name__ == '__main__':
    fixed_data = {
        'pop': 5000000,  # population at risk
        'duration': 500,  # number of days for simulation
        'initial_infections': 4,  # initial number of cases
        'init_contacts': 50,  # contacts without social distancing
        'contagiousness': 0.005,  # prob. of getting disease if exposed
        'days_spreading': 10,  # days contagious after infection
    }
    variable_data = {
        'red_daily_contacts': fixed_data['init_contacts'],  # social distancing
        'red_start': 20,  # start of social distancing
        'red_end': 200,  # end of social distancing
    }

    infections, total_infections = simulation(fixed_data, variable_data)
    fig = plt.figure(figsize=(12, 8.5))
    plot_infections(infections, total_infections, fixed_data)
    plt.show()
