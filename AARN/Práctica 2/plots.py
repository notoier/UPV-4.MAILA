import numpy as np

import plotly.graph_objects as go
import matplotlib.pyplot as plt


### PLOTLY INTERACTIVE GRAPHICS

def create_heatmap():

    # make figure
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    fig_dict["layout"]["xaxis"] = {"range": [-4.5, 4.5], "title": "X1"}
    fig_dict["layout"]["yaxis"] = {"range": [-4.5, 4.5], "title": "X2"}
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["autosize"] = False
    fig_dict["layout"]["width"] = 800
    fig_dict["layout"]["height"] = 800
    
    return fig_dict


def add_heatmap(fig_dict, parameters, forward, epoch=0):
    
    # Check if it is valid to do this visualization
    assert parameters["W1"].shape[1] == 2, f"Please, set input parameter 'visualize' to False. The MLP must have only 2 input values in order to do this visualization (not {parameters['W1'].shape[1]})."
    
    n = 80
    
    xmin, ymin = -4.5, -4.5
    xmax, ymax = 4.5, 4.5

    xstep = (xmax - xmin) / n
    ystep = (ymax - ymin) / n

    grid_values = [[x, y] for x in np.arange(xmin, xmax, xstep) for y in np.arange(ymin, ymax, ystep)]
    grid_values = np.array(grid_values).T
    
    z, _ = forward(grid_values, parameters)
    z = np.reshape(z, (n, n)).T
        
    frame = {"data": [], "name": f'Epoch: {epoch}'}

    data_dict = {
        "type": 'heatmap',
        "x": np.arange(xmin, xmax, xstep).tolist(),
        "y": np.arange(ymin, ymax, ystep).tolist(),
        "z": z,
        "zsmooth": 'best',
        "zmin": 0.0,
        "zmid": 0.5,
        "zmax": 1.0,
        "visible": True,
        "colorscale": 'RdBu',
        "colorbar": dict(thickness=20, ticklen=4),
        "name": f'Epoch: {epoch}'
    }

    frame["data"].append(data_dict)
    fig_dict["data"].append(data_dict)
    fig_dict["frames"].append(frame)

    return fig_dict

def show_heatmap(fig_dict, X, Y, num_iterations, epf=10):

    colors = [['red', 'blue'][elem] for elem in Y[0]]
    total = num_iterations // epf

    # Create and add slider
    sliders_dict = {
        "active": total - 1,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Epoch: ",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 1.0,
        "x": 0,
        "y": 0,
        "steps": []
    }

    for i in range(total):
        step = dict(
            method="update",
            args=[{"visible": [False] * total},
                    {"frame": {"duration": 300, "redraw": True}, 
                     "mode": "animate", 
                     "transition": {"duration": 300}
                     }],  # layout attribute
            label=str(i * epf)
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        step["args"][0]["visible"].append(True)  # Add another trace as "visible"
        sliders_dict["steps"].append(step)
            
    fig_dict["layout"]["sliders"] = [sliders_dict]
    fig = go.Figure(fig_dict)

    fig.add_trace(
        go.Scatter(
            x=X[0,:].T,
            y=X[1,:].T,
            mode='markers',
            marker={"line_width": 2, "size": 10, "color": colors},
            name="Train data"
        )
    )

    return fig


### MATPLOTLIB GRAPHICS

def plot_decision_boundary(model, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[0, :].min() - 1, X[0, :].max() + 1
    y_min, y_max = X[1, :].min() - 1, X[1, :].max() + 1
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid
    Z = model(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.ylabel('x2')
    plt.xlabel('x1')
    plt.scatter(X[0, :], X[1, :], c=y, cmap=plt.cm.Spectral)



