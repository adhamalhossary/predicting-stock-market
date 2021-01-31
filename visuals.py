import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def evaluate(results):
    """
    Visualization code to display results of various learners.

    inputs:
      - results: Dictionary including stats from different learners
    """

    # Create figure
    fig, ax = plt.subplots(2, 3, figsize=(15, 9))

    # Constants
    bar_width = 0.45
    colors = ['#A00000', '#00A0A0', '#00A000']

    # Super loop to plot four panels of data
    for k, learner in enumerate(results.keys()):
        for j, metric in enumerate(['train_time', 'rmse_train', 'mae_train', 'pred_time', 'rmse_test', 'mae_test']):
            # Creative plot code
            ax[j // 3, j % 3].bar(k + bar_width, results[learner][metric], width=bar_width, color=colors[k])

    # Add unique y-labels
    ax[0, 0].set_ylabel("Time (in seconds)")
    ax[0, 1].set_ylabel("RMSE")
    ax[0, 2].set_ylabel("MAE")
    ax[1, 0].set_ylabel("Time (in seconds)")
    ax[1, 1].set_ylabel("RMSE")
    ax[1, 2].set_ylabel("MAE")

    # Hide x-axis
    ax[0, 0].tick_params(bottom=False)
    ax[0, 0].set(xticklabels=[])
    ax[0, 1].tick_params(bottom=False)
    ax[0, 1].set(xticklabels=[])
    ax[0, 2].tick_params(bottom=False)
    ax[0, 2].set(xticklabels=[])
    ax[1, 0].tick_params(bottom=False)
    ax[1, 0].set(xticklabels=[])
    ax[1, 1].tick_params(bottom=False)
    ax[1, 1].set(xticklabels=[])
    ax[1, 2].tick_params(bottom=False)
    ax[1, 2].set(xticklabels=[])

    # Add titles
    ax[0, 0].set_title("Model Training")
    ax[0, 1].set_title("RMSE on Training Subset")
    ax[0, 2].set_title("MAE on Training Subset")
    ax[1, 0].set_title("Model Predicting")
    ax[1, 1].set_title("RMSE on Testing Set")
    ax[1, 2].set_title("MAE on Testing Set")

    # Create patches for the legend
    patches = []
    for i, learner in enumerate(results.keys()):
        patches.append(mpatches.Patch(color=colors[i], label=learner))
    plt.legend(handles=patches, bbox_to_anchor=(-.80, 2.53), \
               loc='upper center', borderaxespad=0., ncol=3, fontsize='x-large')

    # Aesthetics
    plt.suptitle("Performance Metrics for Three Supervised Learning Models", fontsize=16, y=1.10)
    plt.show()