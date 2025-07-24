{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.streamlit
    pkgs.python311Packages.scikit-learn
    pkgs.python311Packages.joblib
    pkgs.python311Packages.numpy
    pkgs.python311Packages.pandas
  ];
}
