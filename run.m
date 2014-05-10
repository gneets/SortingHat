%% Initialization
clear ; close all; clc

%% Setup the parameters you will use for this part of the exercise
num_labels = 2

%% =========== Part 1: Loading and Visualizing Data =============

% Load Training Data
fprintf('Loading and Visualizing Data ...\n')

X = csvread('features.csv');
fprintf('Examples X: %d\n', size(X));
trainingX = X(1:1500, :);
testingX = X(1501:end, :);
fprintf('Training X size is %d\n', size(trainingX));
fprintf('Testing X size is %d\n', size(testingX));

y = csvread('position.csv');
fprintf('Examples Y: %d\n', size(y));
trainingY = y(1:1500, :);
testingY = y(1501:end, :);
fprintf('Training Y size is %d\n', size(trainingY));
fprintf('Testing Y size is %d\n', size(testingY));



fprintf('Program paused. Press enter to continue.\n');
pause;

%% ============ Part 2: Vectorize Logistic Regression ============

fprintf('\nTraining One-vs-All Logistic Regression...\n')

lambda = 0.1;
[all_theta] = oneVsAll(trainingX, trainingY, num_labels, lambda);

fprintf('Program paused. Press enter to continue.\n');
pause;


%% ================ Part 3: Predict for One-Vs-All ================
%  After ...
pred = predictOneVsAll(all_theta, testingX);
fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == testingY)) * 100);

