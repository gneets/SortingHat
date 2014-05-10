function [all_theta] = oneVsAll(X, y, num_labels, lambda)

% Some useful variables
m = size(X, 1);
n = size(X, 2);

% Add ones to the X data matrix
X = [ones(m, 1) X];

all_theta = [];

for c = 1:num_labels
    initial_theta = zeros(n + 1, 1);
    options = optimset('GradObj', 'on', 'MaxIter', 500);
    [theta] = ...
            fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), ...
                  initial_theta, options);
    all_theta = [all_theta; theta'];
endfor















% =========================================================================


end
