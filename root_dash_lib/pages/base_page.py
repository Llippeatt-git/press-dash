'''This page is a template for creating a customized page with multiple panels.
This page deliberately avoids using too many functions to make it easier to
understand how to use streamlit.
'''
# Computation imports
import copy
import importlib
import os
import types

import streamlit as st

from .. import dash_builder

importlib.reload(dash_builder)

def main(config_fp: str, user_utils: types.ModuleType=None):
    '''This is the main function that runs the dashboard.

    Args:
        config_fp: The filepath to the configuration file.
        user_utils: The module containing the user-defined functions.
            Defaults to those in root_dash_lib.
    '''

    ################################################################################
    # Script Setup
    ################################################################################

    # This must be the first streamlit command
    st.set_page_config(layout='wide')

    builder = dash_builder.DashBuilder(config_fp, user_utils=user_utils)

    # Set the title that shows up at the top of the dashboard
    if 'page_title' in builder.config:
        st.title(builder.config['page_title'])

    # Prep data
    preprocessed_df, config = builder.prep_data(builder.config)


    # Global settings
    st.sidebar.markdown('# Data Settings')
    builder.interface.request_data_settings(st.sidebar)

    st.markdown('#### Data Axes')
    builder.interface.request_data_axes(st)

    # ################################################################################
    # # Set up global settings
    # ################################################################################

    # # Get global data settings
    # st.sidebar.markdown( '# Data Settings' )
    # global_data_kw = dash_utils.setup_data_settings( st.sidebar, config, )

    # # Filter settings
    # global_categorical_filter_defaults = {
    #     # 'Award Dept Name': [ 'CIERA', 'P&A',] # CUSTOMIZE (example)
    # }
    # global_numerical_filter_defaults = {}

    # # Global figure settings
    # st.sidebar.markdown( '# Figure Settings' )
    # global_plot_kw = dash_utils.setup_figure_settings( st.sidebar, color_palette=config['color_palette'] )

    # ################################################################################
    # # Actual analysis
    # ################################################################################
    # tag = 'DEFAULT' # CUSTOMIZE (used for distinguishing widgets)

    # # Copy the global settings as the basis for the local
    # data_kw = copy.deepcopy( global_data_kw)
    # plot_kw = copy.deepcopy( global_plot_kw)

    # st.markdown( '#### Data Axes' )
    # # If you know you only want to count or some, delete and replace with e.g.
    # # data_axes_kw['count_or_sum'] == 'Count'
    # data_kw['count_or_sum'] = st.selectbox(
    #     'Do you want to count entries or sum a column?',
    #     [ 'Count', 'Sum' ],
    #     index=0, # CUSTOMIZE
    #     key='{}:count_or_sum'.format( tag ),
    # )
    # if data_kw['count_or_sum'] == 'Count':
    #     data_kw['y_column'] = st.selectbox(
    #         'What do you want to count unique entries of?',
    #         config['id_columns'], # CUSTOMIZE
    #         index=0, # CUSTOMIZE
    #         key='{}:y_column'.format( tag ),
    #             )
    # elif data_kw['count_or_sum'] == 'Sum':
    #     data_kw['y_column'] = st.selectbox(
    #         'What do you want to sum?',
    #         config['weight_columns'], # CUSTOMIZE
    #         index=0, # CUSTOMIZE
    #         key='{}:y_column'.format( tag ),
    #     )
    # data_kw['time_bin_column'] = st.selectbox(
    #     'How do you want to bin the data in time?',
    #     config['time_bin_columns'], # CUSTOMIZE
    #     index=0, # CUSTOMIZE
    #     key='{}:time_bin_column'.format( tag ),
    # )
    # data_kw['groupby_column'] = st.selectbox(
    #     'What do you want to group the data by?',
    #     config['categorical_columns'], # CUSTOMIZE
    #     index=0, # CUSTOMIZE
    #     key='{}:groupby_column'.format( tag ),
    # )

    # # Change categories if requested.
    # # This needs to be done before the figure settings,
    # # but should have no user-facing effect, so it can be outside general_st_col
    # recategorized_df = st.cache_data( data_utils.recategorize_data )(
    #     preprocessed_df,
    #     config['new_categories'],
    #     data_kw['recategorize'],
    #     data_kw['combine_single_categories'],
    # )

    # # Import categorical filter defaults from the global settings, but only if both use the same recategorization settings
    # categorical_filter_defaults = copy.deepcopy( global_categorical_filter_defaults )
    # numerical_filter_defaults = copy.deepcopy( global_numerical_filter_defaults )

    # st.markdown( '#### Filter Settings' )
    # # categorical_filter_defaults = { 'Award Dept Name': [ 'CIERA', 'P&A',] } # CUSTOMIZE (example)
    # # numerical_filter_defaults = { 'Overall Award Reporting Fiscal Year (yyyy)': [ 2013, 2023 ] } # CUSTOMIZE (example)
    # search_str, search_col, categorical_filters, numerical_filters = dash_utils.setup_filters(
    #     st,
    #     recategorized_df,
    #     config,
    #     include_search=False, # CUSTOMIZE
    #     include_categorical_filters=True, # CUSTOMIZE
    #     include_numerical_filters=True, # CUSTOMIZE
    #     categorical_filter_defaults=categorical_filter_defaults,
    #     numerical_filter_defaults=numerical_filter_defaults,
    #     tag=tag,
    # )

    # # Fiter the data
    # selected_df = st.cache_data( data_utils.filter_data )(
    #     recategorized_df,
    #     search_str,
    #     search_col,
    #     categorical_filters,
    #     numerical_filters
    # )

    # # Retrieve counts or sums
    # aggregated_df, total = st.cache_data( time_series_utils.aggregate )(
    #     selected_df,
    #     data_kw['time_bin_column'],
    #     data_kw['y_column'],
    #     data_kw['groupby_column'],
    #     data_kw['count_or_sum'],
    # )

    # st.sidebar.markdown( '## Lineplot Settings' )

    # plot_kw['category_colors'] = {
    #     category: global_plot_kw['color_palette'][i]
    #     for i, category in enumerate( aggregated_df.columns )
    # }

    # lineplot_kw = copy.deepcopy( plot_kw )
    # default_ymax, default_tick_spacing = dash_utils.get_tick_range_and_spacing(
    #     total,
    #     data_kw['cumulative']
    # )
    # lineplot_kw.update({
    #     'x_label': st.sidebar.text_input(
    #         'lineplot x label',
    #         value=data_kw['time_bin_column'], # CUSTOMIZE
    #         key='{}:lineplot_x_label'.format( tag ),
    #     ),
    #     'y_label': st.sidebar.text_input(
    #         'lineplot y label',
    #         value=data_kw['y_column'], # CUSTOMIZE
    #         key='{}:lineplot_y_label'.format( tag ),
    #     ),
    #     'log_yscale': st.sidebar.checkbox(
    #         'use log yscale',
    #         value=False,
    #         key='{}:lineplot_log_yscale'.format( tag ),
    #     ),
    #     'linewidth': st.sidebar.slider(
    #         'linewidth',
    #         0.,
    #         10.,
    #         value=2.,
    #         key='{}:lineplot_linewidth'.format( tag ),
    #     ),
    #     'marker_size': st.sidebar.slider(
    #         'marker size',
    #         0.,
    #         100.,
    #         value=30.,
    #         key='{}:lineplot_marker_size'.format( tag ),
    #     ),
    #     'y_lim': st.sidebar.slider(
    #         'y limits',
    #         0.,
    #         default_ymax*2.,
    #         value=[0., default_ymax ],
    #         key='{}:lineplot_y_lim'.format( tag ),
    #     ),
    #     'tick_spacing': st.sidebar.number_input(
    #         'y tick spacing',
    #         value=default_tick_spacing,
    #         key='{}:lineplot_tick_spacing'.format( tag ),
    #     ),
    # })
    # # Pull in the data dictionary (needed for caching)
    # lineplot_kw.update( data_kw )

    # st.sidebar.markdown( '## Stackplot Settings' )

    # stackplot_kw = copy.deepcopy( plot_kw )
    # stackplot_kw.update({
    #     'x_label': st.sidebar.text_input(
    #         'stackplot x label',
    #         value=data_kw['time_bin_column'], # CUSTOMIZE
    #         key='{}:stackplot_x_label'.format( tag ),
    #     ),
    #     'y_label': st.sidebar.text_input(
    #         'stackplot y label',
    #         value='Fraction of {} of "{}"'.format( data_kw['count_or_sum'], data_kw['y_column'] ), # CUSTOMIZE
    #         key='{}:stackplot_y_label'.format( tag ),
    #     ),
    # })

    # # Pull in the data dictionary (needed for caching )
    # stackplot_kw.update( data_kw )

    # for view in [ 'lineplot', 'stackplot', 'data' ]:

    #     # For datawe include additional options.
    #     if view == 'data':
    #         df_tag = st.radio(
    #             'What data do you want to see?',
    #             [ 'original', 'preprocessed', 'recategorized', 'aggregated' ],
    #             index=0,
    #             horizontal=True,
    #             key='{}:df_tag'.format( tag ),
    #         )
    #     else:
    #         df_tag = 'selected'
    #     download_kw = st.cache_data( time_series_utils.view_time_series )(
    #         view,
    #         df,
    #         preprocessed_df,
    #         selected_df,
    #         aggregated_df,
    #         total,
    #         data_kw,
    #         lineplot_kw,
    #         stackplot_kw,
    #         config,
    #         tag=tag,
    #         df_tag=df_tag,
    #     )
    #     if view == 'data':
    #         download_kw, show_df = download_kw
    #         if st.checkbox( 'View a subset?', value=False, key='{}:view_subset'.format( tag ) ):
    #             try:
    #                 columns_to_show = st.multiselect(
    #                     'Which columns do you want to show?',
    #                     show_df.columns,
    #                     default=[ data_kw['time_bin_column'], data_kw['y_column'], data_kw['groupby_column'] ],
    #                 )
    #             except:
    #                 columns_to_show = st.multiselect(
    #                     'Which columns do you want to show?',
    #                     show_df.columns,
    #                 )

    #             st.write( show_df[ columns_to_show ] )
    #     st.download_button( **download_kw )

    # # Check for the "STOP" environment variable
    # # This is a hack to stop the streamlit app from running
    # if os.environ.get("STOP_STREAMLIT"):
    #     st.stop()